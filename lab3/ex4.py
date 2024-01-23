def build_xml_element(tag, content, **key_values):
    attributes = ' '.join(f'{key}="{value}"' for key, value in key_values.items())
    xml_element = f'<{tag} {attributes}>{content}</{tag}>'
    return xml_element


def main():
    print(build_xml_element("a", "Hello there", href="https://python.org", _class="my-link", id="someid"))


if __name__ == '__main__':
    main()
