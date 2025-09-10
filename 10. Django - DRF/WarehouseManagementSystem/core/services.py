from core.models import Product, Warehouse, ProductMaterial

def calculate_materials(order_list):
    """
    order_list = [
        {"product_code": "238923", "quantity": 30},
        {"product_code": "498723", "quantity": 20},
    ]
    """

    result = []
    # Omborda mavjud partiyalarni global "ishchi nusxa" sifatida olish
    warehouse_data = list(Warehouse.objects.all().order_by("received_date", "id"))

    for order in order_list:
        try:
            product = Product.objects.get(product_code=order["product_code"])
        except Product.DoesNotExist:
            continue

        product_entry = {
            "product_name": product.product_name,
            "product_qty": order["quantity"],
            "product_materials": []
        }

        # mahsulot uchun kerakli barcha xomashyo
        product_materials = ProductMaterial.objects.filter(product=product)

        for pm in product_materials:
            required_qty = pm.quantity * order["quantity"]  # umumiy kerakli miqdor
            material_name = pm.material.material_name

            # partiyalar bo‘yicha taqsimlash
            for w in warehouse_data:
                if w.material_id == pm.material.id and required_qty > 0:
                    if w.remainder >= required_qty:
                        # kerakli hammasini shu partiyadan olish mumkin
                        product_entry["product_materials"].append({
                            "warehouse_id": str(w.id),
                            "material_name": material_name,
                            "qty": required_qty,
                            "price": float(w.price)
                        })
                        # vaqtincha "band" qilish
                        w.remainder -= required_qty
                        required_qty = 0
                        break
                    else:
                        # partiyadagi hammasini olib qolganini keyingidan olish
                        product_entry["product_materials"].append({
                            "warehouse_id": str(w.id),
                            "material_name": material_name,
                            "qty": w.remainder,
                            "price": float(w.price)
                        })
                        required_qty -= w.remainder
                        w.remainder = 0

            # Agar omborda qolmagan bo‘lsa
            if required_qty > 0:
                product_entry["product_materials"].append({
                    "warehouse_id": None,
                    "material_name": material_name,
                    "qty": required_qty,
                    "price": None
                })

        result.append(product_entry)

    return {"result": result}
