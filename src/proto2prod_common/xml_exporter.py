import xml.etree.ElementTree as ET

def dict_to_xml(data: dict, root_tag: str = 'root') -> str:
    """Convert a dict to an XML string."""
    root = ET.Element(root_tag)
    def _build(elem, d):
        for k, v in d.items():
            child = ET.SubElement(elem, k)
            if isinstance(v, dict):
                _build(child, v)
            else:
                child.text = str(v)
    _build(root, data)
    return ET.tostring(root, encoding='utf-8').decode('utf-8')
