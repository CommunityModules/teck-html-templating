from binhex import openrsrc
from datetime import tzinfo, datetime
import os
import jinja2

J2 = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
)

TYPE_PUBLIC_IP_REPORT = "report_public_ip"
TYPE_INDEX_PAGE = "report_index"
TYPE_IMAGE_REPORT = "report_image"

ALLOWED_TYPES = [{
    "key": TYPE_PUBLIC_IP_REPORT,
    "template_file": "report_public_ip.html"
}, {
    "key": TYPE_INDEX_PAGE,
    "template_file": "report_index.html"
}, {
    "key": TYPE_IMAGE_REPORT,
    "template_file": "report_image.html"
}]


def get_template_types():
    template_types = []
    for obj in ALLOWED_TYPES:
        if "key" in obj:
            template_types.append(obj["key"])
    return template_types

def generate(template_type, data):
    _the_type = None

    for _type in ALLOWED_TYPES:
        if _type["key"] == template_type:
            _the_type = _type

    if _the_type is None:
        raise FileNotFoundError()

    template = J2.get_template(_the_type['template_file'])
    return template.render({'content': data})


def main():
    pip_struct = {
        "content": [{
            "location": "centralus",
            "method": "Static",
            "name": "ffffffff-0000-ffff-0000-ffffffffffff",
            "pip_type": "loadBalancers",
            "sku": "Standard",
            "state": "Succeeded",
            "tags": {
                "environment": "development",
                "project": "shared",
                "terraform": "true"
            },
            "type": "Microsoft.Network/publicIPAddresses"
        }
        ]
    }

    result = generate(template_type=TYPE_PUBLIC_IP_REPORT, data=pip_struct['content'])
    print(result)


if __name__ == '__main__':
    main()
