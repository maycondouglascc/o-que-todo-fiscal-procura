(() => {
  'use strict';
  const productId = 'o-que-todo-fiscal-procura';
  const params = new URLSearchParams(window.location.search);
  const allowed = key => /^utm_(source|medium|campaign|term|content|id|source_platform|creative_format|marketing_tactic)$/.test(key) || ['fbclid', 'gclid', '_gl'].includes(key);
  const attribution = {};
  params.forEach((value, key) => { if (allowed(key)) attribution[key] = value; });
  const trackMeta = (event, detail = {}) => {
    if (typeof window.fbq === 'function') window.fbq('track', event, {
      content_ids: [productId],
      content_type: 'product',
      ...detail
    });
  };
  // Local instrumentation only. No ad or analytics service is configured without verified IDs.
  window.dataLayer = window.dataLayer || [];
  function emit(event, detail = {}) {
    const payload = { event, content_id: productId, content_type: 'product', ...detail, attribution };
    window.dataLayer.push(payload);
    window.dispatchEvent(new CustomEvent('guia:analytics', { detail: payload }));
  }
  const headlineVariant = params.get('headline') === 'controle' ? 'controle' : 'seguranca';
  if (headlineVariant === 'controle') {
    document.getElementById('hero-title').textContent = 'Confira os pontos essenciais da sua NFS-e antes de enviá-la.';
  }
  const audienceVariant = params.get('publico') === 'contadores' ? 'contadores' : 'prestadores';
  if (audienceVariant === 'contadores') {
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
    const trackCheckoutClick = () => {
      emit('CTA_Click', { cta_location: link.dataset.cta, ...variants });
      emit('CheckoutOutbound', { cta_location: link.dataset.cta, checkout_url: destination.origin + destination.pathname, ...variants });
      trackMeta('InitiateCheckout', { cta_location: link.dataset.cta, value: 47, currency: 'BRL' });
    };
    link.addEventListener('click', trackCheckoutClick);
    link.addEventListener('auxclick', event => { if (event.button === 1) trackCheckoutClick(); });
  });
  // The payment provider remains the source of truth for approval. A verified
  // checkout integration can call this hook after approval; clicks never emit Purchase.
  window.growthCouncil = window.growthCouncil || {};
  const recordedPurchaseIds = new Set();
  window.growthCouncil.recordApprovedPurchase = (details = {}) => {
    const transactionId = details.transaction_id;
    if (transactionId && recordedPurchaseIds.has(transactionId)) return false;
    if (transactionId) recordedPurchaseIds.add(transactionId);
    emit('Purchase', { ...details, ...variants });
    return true;
  };
  // Optional return bridge: configure the provider to redirect here only after
  // approval, with gc_purchase=approved and its own transaction_id/value/currency.
  // Without a provider-issued transaction_id this path remains inert.
  if (params.get('gc_purchase') === 'approved' && params.get('transaction_id')) {
    const value = Number(params.get('value'));
    window.growthCouncil.recordApprovedPurchase({
      transaction_id: params.get('transaction_id'),
      ...(Number.isFinite(value) ? { value } : {}),
      currency: params.get('currency') || 'BRL',
      source: params.get('source') || 'checkout'
    });
  }
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
