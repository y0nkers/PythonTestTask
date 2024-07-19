import os
import sys
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit


def create_spark_session():
    return SparkSession.builder \
        .appName("task2") \
        .getOrCreate()

def create_dataframes(spark):
    # Продукты (id, name)
    products_data = [
        (1, 'Яблоко'), (2, 'Банан'), (3, 'Морковь'), (4, 'Баклажан'),
        (5, 'Виноград'), (6, 'Дыня'), (7, 'Лимон'), (8, 'Клавиатура')
    ]
    
    # Категории (id, name)
    categories_data = [
        (1, 'Фрукты'), (2, 'Овощи')
    ]
    
    # Связи (product_id, category_id)
    refs_data = [
        (1, 1), (2, 1), (3, 2), (4, 2), 
        (5, 1), (6, 1), (7, 1)
    ]

    products = spark.createDataFrame(products_data, ["id", "name"])
    categories = spark.createDataFrame(categories_data, ["id", "name"])
    refs = spark.createDataFrame(refs_data, ["product_id", "category_id"])
    
    return products, categories, refs

def get_data(products, categories, refs):
    return get_pairs(products, categories, refs), get_no_pairs(products, refs)

# Пары "имя продукта - имя категории"
def get_pairs(products, categories, refs):
    return products.join(
        refs, products.id == refs.product_id, how='left'
    ).join(
        categories, refs.category_id == categories.id, how='left'
    ).select(
        products.name.alias('Продукты'), categories.name.alias('Категории')
    ).filter(
        col('Категории').isNotNull()
    ).orderBy(col('Продукты'))

# Продукты без категорий
def get_no_pairs(products, refs):
    return products.join(
        refs, products.id == refs.product_id, how='left_anti'
    ).select(products.name.alias('Продукты'))

def main():
    spark = create_spark_session()
    products, categories, refs = create_dataframes(spark)
    
    pairs, no_pairs = get_data(products, categories, refs)
    
    print("Пары продукт-категория:")
    pairs.show()

    print("Продукты без категории:")
    no_pairs.show()

if __name__ == "__main__":
    main()
