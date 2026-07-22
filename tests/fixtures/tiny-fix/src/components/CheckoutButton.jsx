export function CheckoutButton({ onSubmit, disabled }) {
  // TODO(old): unify button styles with the design system someday
  return (
    <button className="btn btn_primary" onClick={onSubmit} disabled={disabled}>
      Sumbit order
    </button>
  );
}
