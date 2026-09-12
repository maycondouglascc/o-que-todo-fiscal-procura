# Checkout bridge

The landing page intentionally does not emit `Purchase` on CTA click. The payment provider is the source of truth.

## Required integration

After the provider confirms an approved payment, the application or thank-you page must call:

```js
window.growthCouncil?.recordApprovedPurchase({
  transaction_id: 'provider-transaction-id',
  value: 47,
  currency: 'BRL',
  source: 'herospark'
});
```

`transaction_id`, `value`, `currency` and `source` must come from the provider. Do not populate them from the outbound CTA. If the provider cannot call this hook, reconcile its sales export with the landing-page attribution instead and record the method in `inputs/IMPLEMENTATION_INPUTS.md`.

For a provider redirect, the return URL must include `gc_purchase=approved`, a provider-issued `transaction_id`, and, when available, `value`, `currency` and `source`. Any return without the approved flag and transaction ID is ignored.

## Acceptance criteria

- A click produces `CTA_Click` and `CheckoutOutbound` only.
- An approved payment produces one `Purchase` with a provider transaction ID.
- Duplicate callbacks are deduplicated by transaction ID in the production analytics layer.
- Refunds are recorded separately and do not overwrite the original purchase event.
