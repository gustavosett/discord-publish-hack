

class ANSI():
    
    def background(code):
        return f"\33[{code}m"
    
    def style_text(code):
        return f"\33[{code}m"
    
    def color_text(code):
        return f"\33[{code}m"