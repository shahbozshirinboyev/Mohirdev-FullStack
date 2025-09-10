from core.models import Product, Warehouse, ProductMaterial

def calculate_materials(order_list):
    if not order_list:
        return {"result": [], "message": "Hech qanday buyurtma yuborilmadi"}

    if isinstance(order_list, dict):
        order_list = [order_list]

    result = []
    warehouse_data = list(Warehouse.objects.all().order_by("received_date", "id"))

    for order in order_list:
        if "product_code" not in order or "quantity" not in order:
            result.append({
                "order": order,
                "error": "product_code va quantity majburiy maydonlar"
            })
            continue

        try:
            product = Product.objects.get(product_code=order["product_code"])
        except Product.DoesNotExist:
            result.append({
                "product_code": order["product_code"],
                "product_qty": order["quantity"],
                "error": f"Mahsulot topilmadi (product_code={order['product_code']})"
            })
            continue

        product_entry = {
            "product_name": product.product_name,
            "product_code": product.product_code,
            "product_qty": order["quantity"],
            "product_materials": []
        }

        product_materials = ProductMaterial.objects.filter(product=product)

        for pm in product_materials:
            required_qty = pm.quantity * order["quantity"]
            material_name = pm.material.material_name

            for w in warehouse_data:
                if w.material_id == pm.material.id and required_qty > 0:
                    if w.remainder >= required_qty:
                        product_entry["product_materials"].append({
                            "warehouse_id": str(w.id),
                            "material_name": material_name,
                            "qty": required_qty,
                            "price": float(w.price)
                        })
                        w.remainder -= required_qty
                        required_qty = 0
                        break
                    else:
                        product_entry["product_materials"].append({
                            "warehouse_id": str(w.id),
                            "material_name": material_name,
                            "qty": w.remainder,
                            "price": float(w.price)
                        })
                        required_qty -= w.remainder
                        w.remainder = 0

            if required_qty > 0:
                product_entry["product_materials"].append({
                    "warehouse_id": None,
                    "material_name": material_name,
                    "qty": required_qty,
                    "price": None
                })

        result.append(product_entry)

    return {"result": result}