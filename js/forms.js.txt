/**
 * forms.js — Intent-based form rendering system
 *
 * When the backend detects a form intent (quote, contact, etc.),
 * it returns { type: "form", formId: "...", message: "..." }.
 * This module renders the matching form inline in the chat bubble,
 * handles validation, submission, and confirmation.
 */

'use strict';

const FORMS = (() => {
  let currentFormId = null;
  let currentFormDef = null;
  let isSubmitting = false;
  const formCache = {};

  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  async function fetchFormDefinition(formId) {
    if (formCache[formId]) return formCache[formId];

    try {
      const formDef = await API.getForm(formId);
      formCache[formId] = formDef;
      return formDef;
    } catch (err) {
      console.warn('Backend form fetch failed, using fallback:', err);
      return getFallbackForm(formId);
    }
  }

  function getFallbackForm(formId) {
    const fallbacks = {
      tile_quote: {
        id: 'tile_quote',
        title: 'Tile Quote Request',
        description: 'Please complete the details below so we can prepare an accurate quote.',
        fields: [
          { name: 'customerName', label: 'Your full name', type: 'text', required: true, placeholder: 'e.g. John Smith' },
          { name: 'phone', label: 'Contact number', type: 'tel', required: true, placeholder: 'e.g. 082 123 4567' },
          { name: 'email', label: 'Email address', type: 'email', required: false, placeholder: 'e.g. john@email.com' },
          { name: 'area', label: 'Which area or suburb are you in?', type: 'text', required: true, placeholder: 'e.g. Durbanville, Cape Town' },
          { name: 'productType', label: 'What are you looking for?', type: 'select', options: ['Tiles', 'Vinyl Flooring', 'Laminate Flooring', 'Sanitaryware', 'Adhesives & Grout', 'Not sure — need advice'], required: true },
          { name: 'roomType', label: 'Which room or area is this for?', type: 'select', options: ['Bathroom', 'Kitchen', 'Lounge / Living room', 'Bedroom', 'Outdoor / Patio', 'Commercial space', 'Multiple areas', 'Other'], required: true },
          { name: 'sqm', label: 'Approximate square metres needed', type: 'number', required: false, placeholder: 'e.g. 25' },
          { name: 'preferredStore', label: 'Preferred Tiletoria branch', type: 'select', options: ['Any branch', 'Cape Town — N1 City', 'Cape Town — Ottery', 'Cape Town — Montague Gardens', 'Johannesburg — Randburg', 'Johannesburg — Boksburg', 'Durban — The Bridge', 'Port Elizabeth', 'Pretoria — Centurion'], required: false },
          { name: 'message', label: 'Tell us more about your project', type: 'textarea', required: true, placeholder: 'Describe what you need — tile type, colour preference, surface preparation needed, etc.' },
          { name: 'consent', label: 'I consent to Tiletoria processing my personal information in accordance with the POPI Act. I understand my information will be used solely to respond to this quote request.', type: 'checkbox', required: true },
        ]
      },
      contact_me: {
        id: 'contact_me',
        title: 'Contact Request',
        description: 'Leave your details and a Tiletoria consultant will contact you shortly.',
        fields: [
          { name: 'customerName', label: 'Your full name', type: 'text', required: true, placeholder: 'e.g. John Smith' },
          { name: 'phone', label: 'Contact number', type: 'tel', required: true, placeholder: 'e.g. 082 123 4567' },
          { name: 'email', label: 'Email address', type: 'email', required: false, placeholder: 'e.g. john@email.com' },
          { name: 'area', label: 'Your area or suburb', type: 'text', required: true, placeholder: 'e.g. Randburg, Johannesburg' },
          { name: 'preferredTime', label: 'Best time to contact you?', type: 'select', options: ['Morning (8am – 12pm)', 'Afternoon (12pm – 5pm)', 'Anytime', 'Specific time — I\'ll explain below'], required: true },
          { name: 'enquiryType', label: 'What is this regarding?', type: 'select', options: ['Product enquiry', 'Quote request', 'Order status', 'Complaint / Issue', 'General question', 'Business account'], required: true },
          { name: 'message', label: 'How can we help you?', type: 'textarea', required: true, placeholder: 'Briefly describe what you need assistance with...' },
          { name: 'consent', label: 'I consent to Tiletoria processing my personal information in accordance with the POPI Act.', type: 'checkbox', required: true },
        ]
      },
    };
    return fallbacks[formId] || null;
  }

  async function showForm(formId, messageText) {
    const msgRow = CHAT.addMessage('bot', messageText || '');

    const formDef = await fetchFormDefinition(formId);
    if (!formDef) {
      CHAT.addErrorMessage(`Sorry, I couldn't load the form (ID: ${formId}). Please try again or contact us directly.`);
      return;
    }

    currentFormId = formId;
    currentFormDef = formDef;

    const formContainer = document.createElement('div');
    formContainer.className = 'chat-form-container';
    formContainer.id = `form-${formId}`;
    formContainer.innerHTML = buildFormHTML(formDef);

    const lastBotRow = document.querySelector('#chat-messages .msg-row.bot:last-child .msg-body');
    if (lastBotRow) {
      lastBotRow.appendChild(formContainer);
    } else {
      document.getElementById('chat-messages').appendChild(formContainer);
    }

    CHAT.scrollToBottom?.() || scrollToBottom();

    bindFormEvents(formContainer, formId);
  }

  function buildFormHTML(formDef) {
    const fields = formDef.fields || [];
    let fieldsHTML = '';

    fields.forEach(field => {
      fieldsHTML += renderField(field);
    });

    const honeypot = `<div class="form-honeypot" aria-hidden="true"><input type="text" name="_gotcha" tabindex="-1" autocomplete="off"></div>`;

    return `
      <div class="chat-form-header">
        <div class="chat-form-icon"><i class="fas fa-clipboard-list"></i></div>
        <div class="chat-form-title">${escapeHtml(formDef.title)}</div>
      </div>
      <div class="chat-form-body">
        ${honeypot}
        ${fieldsHTML}
        <div class="chat-form-error hidden" id="form-error-${formDef.id}"></div>
        <div class="chat-form-actions">
          <button type="button" class="btn-primary full-width chat-form-submit" data-form="${escapeHtml(formDef.id)}">
            <i class="fas fa-paper-plane"></i> Submit Request
          </button>
        </div>
      </div>
    `;
  }

  function renderField(field) {
    const requiredAttr = field.required ? 'required' : '';
    const requiredLabel = field.required ? ' <span class="required-mark">*</span>' : '';
    const fieldId = `field-${field.name}`;

    switch (field.type) {
      case 'select':
        return `
          <div class="chat-form-group">
            <label class="chat-form-label" for="${fieldId}">${escapeHtml(field.label)}${requiredLabel}</label>
            <select class="chat-form-select" id="${fieldId}" name="${escapeHtml(field.name)}" ${requiredAttr}>
              <option value="">-- Select --</option>
              ${(field.options || []).map(opt => `<option value="${escapeHtml(opt)}">${escapeHtml(opt)}</option>`).join('')}
            </select>
          </div>
        `;

      case 'textarea':
        return `
          <div class="chat-form-group">
            <label class="chat-form-label" for="${fieldId}">${escapeHtml(field.label)}${requiredLabel}</label>
            <textarea class="chat-form-textarea" id="${fieldId}" name="${escapeHtml(field.name)}" placeholder="${escapeHtml(field.placeholder || '')}" ${requiredAttr} rows="3"></textarea>
          </div>
        `;

      case 'checkbox':
        return `
          <div class="chat-form-group">
            <label class="chat-form-checkbox-label">
              <input type="checkbox" id="${fieldId}" name="${escapeHtml(field.name)}" ${requiredAttr}>
              <span class="checkmark"></span>
              <span class="checkbox-text">${escapeHtml(field.label)} ${requiredLabel}</span>
            </label>
          </div>
        `;

      case 'date':
        return `
          <div class="chat-form-group">
            <label class="chat-form-label" for="${fieldId}">${escapeHtml(field.label)}${requiredLabel}</label>
            <input type="date" class="chat-form-input" id="${fieldId}" name="${escapeHtml(field.name)}" ${requiredAttr}>
          </div>
        `;

      default:
        return `
          <div class="chat-form-group">
            <label class="chat-form-label" for="${fieldId}">${escapeHtml(field.label)}${requiredLabel}</label>
            <input type="${field.type}" class="chat-form-input" id="${fieldId}" name="${escapeHtml(field.name)}" placeholder="${escapeHtml(field.placeholder || '')}" ${requiredAttr}>
          </div>
        `;
    }
  }

  function bindFormEvents(container, formId) {
    const submitBtn = container.querySelector('.chat-form-submit');
    if (submitBtn) {
      submitBtn.addEventListener('click', () => handleSubmit(container, formId));
    }

    container.querySelectorAll('input:not([type="checkbox"])').forEach(input => {
      input.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
          e.preventDefault();
          handleSubmit(container, formId);
        }
      });
    });
  }

  function validateForm(container, formDef) {
    const errors = [];
    const data = {};
    const fields = formDef.fields || [];

    fields.forEach(field => {
      const input = container.querySelector(`[name="${field.name}"]`);
      if (!input) return;

      let value;
      if (field.type === 'checkbox') {
        value = input.checked;
      } else {
        value = input.value.trim();
      }

      data[field.name] = value;

      if (field.required) {
        if (field.type === 'checkbox') {
          if (!value) errors.push(`${field.label} must be accepted`);
        } else if (!value) {
          errors.push(`${field.label} is required`);
        }
      }

      if (value && field.type === 'email') {
        const emailRe = /^[\w\.-]+@[\w\.-]+\.\w+$/;
        if (!emailRe.test(value)) errors.push(`${field.label} must be a valid email`);
      }

      if (value && field.type === 'tel') {
        const digits = value.replace(/\D/g, '');
        if (digits.length < 10) errors.push(`${field.label} must have at least 10 digits`);
      }
    });

    const gotcha = container.querySelector('input[name="_gotcha"]');
    if (gotcha && gotcha.value) {
      errors.push('Spam detected');
    }

    return { valid: errors.length === 0, errors, data };
  }

  async function handleSubmit(container, formId) {
    if (isSubmitting) return;

    const validation = validateForm(container, currentFormDef);
    const errorEl = container.querySelector(`#form-error-${formId}`);

    if (!validation.valid) {
      if (errorEl) {
        errorEl.innerHTML = `<i class="fas fa-exclamation-circle"></i> ${escapeHtml(validation.errors[0])}`;
        errorEl.classList.remove('hidden');
      }
      return;
    }

    if (errorEl) errorEl.classList.add('hidden');

    isSubmitting = true;
    const submitBtn = container.querySelector('.chat-form-submit');
    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Sending...';
    }

    try {
      const result = await API.submitForm(formId, validation.data);

      if (result.success) {
        container.innerHTML = `
          <div class="chat-form-success">
            <div class="chat-form-success-icon"><i class="fas fa-check-circle"></i></div>
            <div class="chat-form-success-title">Thank you!</div>
            <div class="chat-form-success-message">${escapeHtml(result.message)}</div>
            <div class="chat-form-success-ref">Ref: ${escapeHtml(result.submission_id?.slice(0, 8) || '')}</div>
          </div>
        `;

        setTimeout(() => {
          CHAT.addMessage('bot', result.message);
        }, 500);

      } else {
        const errorMsg = result.errors?.[0] || 'Submission failed. Please try again.';
        if (errorEl) {
          errorEl.innerHTML = `<i class="fas fa-exclamation-circle"></i> ${escapeHtml(errorMsg)}`;
          errorEl.classList.remove('hidden');
        }
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = '<i class="fas fa-paper-plane"></i> Submit Request';
        }
      }
    } catch (err) {
      console.error('Form submission error:', err);
      if (errorEl) {
        errorEl.innerHTML = `<i class="fas fa-exclamation-circle"></i> Network error. Please try again.`;
        errorEl.classList.remove('hidden');
      }
      if (submitBtn) {
        submitBtn.disabled = false;
        submitBtn.innerHTML = '<i class="fas fa-paper-plane"></i> Submit Request';
      }
    } finally {
      isSubmitting = false;
    }
  }

  async function demoSubmitForm(formId, data) {
    await new Promise(r => setTimeout(r, 800 + Math.random() * 700));

    if (!data.customerName || !data.phone) {
      return { success: false, errors: ['Name and phone are required'] };
    }
    if (data.consent !== true && data.consent !== 'on') {
      return { success: false, errors: ['Please accept the consent checkbox'] };
    }

    return {
      success: true,
      submission_id: 'demo-' + Math.random().toString(36).slice(2, 10),
      message: 'Thank you! We\'ve received your request and one of our team members will contact you shortly.',
    };
  }

  function scrollToBottom() {
    const container = document.getElementById('chat-messages');
    if (container) {
      requestAnimationFrame(() => {
        container.scrollTop = container.scrollHeight;
      });
    }
  }

  return {
    showForm,
    demoSubmitForm,
  };
})();

window.FORMS = FORMS;