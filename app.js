(() => {
  'use strict';
  const productId = 'o-que-todo-fiscal-procura';
  const params = new URLSearchParams(window.location.search);
  const allowed = key => /^utm_(source|medium|campaign|term|content|id|source_platform|creative_format|marketing_tactic)$/.test(key) || ['fbclid', 'gclid', '_gl'].includes(key);
  const attribution = {};
  params.forEach((value, key) => { if (allowed(key)) attribution[key] = value; });
  // Local instrumentation only. No ad or analytics service is configured without verified IDs.
  window.dataLayer = window.dataLayer || [];
  function emit(event, detail = {}) {
    const payload = { event, content_id: productId, content_type: 'product', ...detail, attribution };
    window.dataLayer.push(payload);
    window.dispatchEvent(new CustomEvent('guia:analytics', { detail: payload }));
  }
  const headlineVariant = params.get('headline') === 'controle' ? 'controle' : 'seguranca';
  if (headlineVariant === 'controle') {
    document.getElementById('hero-title').textContent = 'Identifique os erros que mais chamam atenção da fiscalização antes que virem pendências, juros ou multas.';
  }
  const audienceVariant = params.get('publico') === 'contadores' ? 'contadores' : 'prestadores';
  if (audienceVariant === 'contadores') {
    document.querySelector('.hero .eyebrow').lastChild.textContent = ' PARA QUEM ORIENTA A EMISSÃO DE NFS-e';
    document.getElementById('hero-description').textContent = 'Uma referência para orientar seus clientes sobre erros de emissão, cuidados cadastrais e revisão mensal das notas fiscais de serviço.';
  }
  const authorityVariant = params.get('autoridade') === 'secao' ? 'secao' : 'resumida';
  if (authorityVariant === 'secao') document.querySelector('.author-mini').hidden = true;
  const variants = { headline_variant: headlineVariant, audience_variant: audienceVariant, authority_variant: authorityVariant };
  emit('PageView', variants);
  emit('ViewContent', variants);
  document.querySelectorAll('[data-cta]').forEach(link => {
    const destination = new URL(link.href);
    Object.entries(attribution).forEach(([key, value]) => destination.searchParams.set(key, value));
    link.href = destination.toString();
    link.addEventListener('click', () => emit('CTA_Click', { cta_location: link.dataset.cta, ...variants }));
    link.addEventListener('auxclick', event => { if (event.button === 1) emit('CTA_Click', { cta_location: link.dataset.cta, ...variants }); });
  });
  // InitiateCheckout belongs on the real checkout load. Purchase only after payment approval.
  // Never equate an outbound click, payment-method selection, or generated PIX with a purchase.
  const sticky = document.getElementById('sticky-buy');
  const primaryCtas = [...document.querySelectorAll('[data-cta]:not([data-cta="sticky"])')];
  const mobile = window.matchMedia('(max-width: 767px)');
  let scheduled = false;
  function updateSticky() {
    const passedFirstFold = window.scrollY >= window.innerHeight;
    const primaryVisible = primaryCtas.some(link => {
      const rect = link.getBoundingClientRect();
      return rect.bottom > 0 && rect.top < window.innerHeight && rect.right > 0 && rect.left < window.innerWidth;
    });
    const show = mobile.matches && passedFirstFold && !primaryVisible;
    sticky.hidden = !show;
    document.body.classList.toggle('has-sticky', show);
    scheduled = false;
  }
  const requestUpdate = () => { if (!scheduled) { scheduled = true; requestAnimationFrame(updateSticky); } };
  window.addEventListener('scroll', requestUpdate, { passive: true });
  window.addEventListener('resize', requestUpdate, { passive: true });
  document.querySelectorAll('details').forEach(el => el.addEventListener('toggle', requestUpdate));
  document.addEventListener('load', requestUpdate, true);
  updateSticky();
})();
