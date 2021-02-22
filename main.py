import render
import generator

def startup():
    grid = generator.generate(50, 50)
    render.render(grid)
    
def main():
    pass

if __name__ == "__main__":
    startup()