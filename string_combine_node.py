
class StringCombineNew:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "string1": ("STRING", {
                    "default": "",
                    "multiline": True, #True if you want the field to look like the one on the ClipTextEncode node
                    "lazy": True

                }),
                "string2": ("STRING", {
                    "default": "",
                    "multiline": True, #True if you want the field to look like the one on the ClipTextEncode node
                    "lazy": True
                }),
                "separator": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "lazy": True
                }),
                "number_test": ("INT", {
                    "default": 0, 
                    "min": 0, #Minimum value
                    "max": 4096, #Maximum value
                    "step": 64, #Slider's step
                    "display": "number", # Cosmetic only: display as "number" or "slider"
                    "lazy": True # Will only be evaluated if check_lazy_status requires it
                })
            }
        }

    RETURN_TYPES = ("STRING")
    RETURN_NAMES = ("Final String")

    FUNCTION ="run"

    CATEGORY = "CalebCustomNodes"

    def run(self, string1, string2, separator):
        new_string = f"{string1}{separator}{string2}"
        return (new_string)
    

    # A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "StringCombineNew": StringCombineNew
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "StringCombineNew": "Caleb First Custom Node"
}



