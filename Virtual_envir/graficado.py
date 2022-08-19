from bokeh.plotting import figure, output_file, show

if __name__ == '__main__':
    output_file('graficado.html')
    fig = figure()

    total_values = int(input('Cuantos valores se van a graficar:  '))
    x_vals = list(range(total_values))
    y_values = []

    for x in x_vals:
        value = int(input(f'Ingrese el valor Y para {x}: --> '))
        y_values.append(value)

    fig.line(x_vals, y_values, line_width=2)
    show(fig)