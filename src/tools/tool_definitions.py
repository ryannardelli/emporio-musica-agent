PRODUCT_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_products",
            "description": "Busca produtos pelo nome ou categoria.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Nome ou categoria do produto."
                    }
                },
                "required": ["name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_products_by_max_price",
            "description": "Busca produtos disponíveis até determinado preço.",
            "parameters": {
                "type": "object",
                "properties": {
                    "max_price": {
                        "type": "number",
                        "description": "Preço máximo dos produtos."
                    }
                },
                "required": ["max_price"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_product_by_name",
            "description": "Busca um produto específico pelo nome.",
            "parameters": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "object",
                        "description": "Nome do produto."
                    }
                },
                "required": ["name"]
            }
        }
    }
]