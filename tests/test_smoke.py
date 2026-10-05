def test_smoke():
    from PIL import Image
    from lambdawalker.draw.color.HSLuvColor import HSLuvColor
    from lambdawalker.draw.shapes.draw_random_country_blured_contour import draw_random_country_blured_contour
    
    color = HSLuvColor(100, 50, 50)
    assert color.to_rgba() == (112, 123, 81, 255)
    
    img = Image.new("RGBA", (500, 500), (0, 0, 0, 0))
    res = draw_random_country_blured_contour(img, color)
    assert res["color"] is not None
    print("draw OK")
