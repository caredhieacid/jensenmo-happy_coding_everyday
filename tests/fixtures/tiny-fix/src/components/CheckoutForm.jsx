import { CheckoutButton } from "./CheckoutButton";

export function CheckoutForm({ cart, onSubmit }) {
  var itemCount = cart.items.length; // legacy var, intentionally left untouched
  return (
    <form>
      <p>{itemCount} items in your cart</p>
      <CheckoutButton onSubmit={onSubmit} disabled={itemCount === 0} />
    </form>
  );
}
