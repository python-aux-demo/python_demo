def display_photo(
    link: str,
    title: str = None,
) -> None:
    from PIL import Image
    from io import BytesIO
    from urllib.request import urlopen
    import matplotlib.pyplot as plt

    f = urlopen(link)
    b = BytesIO(f.read())
    i = Image.open(b)
    _, ax = plt.subplots(figsize=(8,8))
    ax.axis('off')
    ax.imshow(i)
    if title is not None:
        ax.set_title(title, fontsize=20)