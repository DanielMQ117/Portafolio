"""Calcular descuentos según el monto de compra con if-elifelse."""

monto = float(input("Ingresa el monto de la compra: $"))

# Calcular el descuento según el monto
if monto >= 500:
    descuento = 0.20  # 20%
elif monto >= 300:
    descuento = 0.15  # 15%
elif monto >= 100:
    descuento = 0.10  # 10%
else:
    descuento = 0.0   # Sin descuento

# Calcular el monto descontado y el total a pagar
monto_descuento = monto * descuento
total_pagar = monto - monto_descuento

# Mostrar resultados
print(f"\nDescuento aplicado: {descuento * 100:.0f}%")
print(f"Monto descontado: ${monto_descuento:.2f}")
print(f"Total a pagar: ${total_pagar:.2f}")
