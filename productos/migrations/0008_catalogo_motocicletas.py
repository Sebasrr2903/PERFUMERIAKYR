from django.db import migrations, models


def convertir_categorias(apps, schema_editor):
    Producto = apps.get_model("productos", "Producto")
    Producto.objects.filter(categoria="dulce").update(categoria="vestimenta")
    Producto.objects.filter(categoria="salado").update(categoria="accesorios")


class Migration(migrations.Migration):
    dependencies = [("productos", "0007_normalizar_categorias")]

    operations = [
        migrations.RenameField(
            model_name="producto", old_name="es_combo", new_name="es_kit"
        ),
        migrations.RenameField(
            model_name="producto", old_name="opciones_bebida", new_name="variantes"
        ),
        migrations.RunPython(convertir_categorias, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="producto",
            name="categoria",
            field=models.CharField(
                choices=[
                    ("cascos", "Cascos"),
                    ("vestimenta", "Vestimenta"),
                    ("proteccion", "Protección"),
                    ("accesorios", "Accesorios"),
                    ("repuestos", "Repuestos"),
                ],
                max_length=20,
            ),
        ),
    ]
