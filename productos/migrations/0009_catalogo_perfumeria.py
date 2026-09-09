from django.db import migrations, models

def convertir_categorias(apps, schema_editor):
    Producto = apps.get_model("productos", "Producto")
    equivalencias = {"cascos": "hombre", "vestimenta": "mujer", "proteccion": "unisex", "accesorios": "arabes", "repuestos": "sets"}
    for anterior, nueva in equivalencias.items():
        Producto.objects.filter(categoria=anterior).update(categoria=nueva)

class Migration(migrations.Migration):
    dependencies = [("productos", "0008_catalogo_motocicletas")]
    operations = [
        migrations.RunPython(convertir_categorias, migrations.RunPython.noop),
        migrations.AlterField(model_name="producto", name="categoria", field=models.CharField(choices=[("mujer", "Mujer"), ("hombre", "Hombre"), ("unisex", "Unisex"), ("arabes", "Perfumes árabes"), ("sets", "Sets de regalo")], max_length=20)),
    ]
