import os
import jinja2

J2 = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
)

TYPE_PUBLIC_IP_REPORT = "report_public_ip"

ALLOWED_TYPES = [{
    'key': 'secops_instance_details',
    'template_file': 'secops_instance_details.html'
}, {
    "key": TYPE_PUBLIC_IP_REPORT,
    "template_file": "report_public_ip.html"
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
    example_struct = {
        'content': {
            'ssh_key': """-----BEGIN THIS IS NOT A KEY-----
    HAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLOR
    HAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLOR
    HAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLOR
    HAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLOR
    HAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLORHAPPYJOESPIZZAPARLOR
    -----END THIS IS NOT A KEY-----""",
            'ip_address': '192.168.1.100',
            'urls': {
                'approve': 'https://example/?a=b&c=d',
                'reject': 'https://example/?1=2&3=4',
            }
        }
    }

    pip_struct = {
        "content": [{
            "location": "centralus",
            "method": "Static",
            "name": "a4bad379-7edf-40d2-8bc6-00251fbe4a18",
            "pip_type": "loadBalancers",
            "sku": "Standard",
            "state": "Succeeded",
            "tags": {
                "aks-managed-cluster-name": "aks-shared-edo-dev-d1da",
                "aks-managed-cluster-rg": "rg-shared-edo-dev-d1da",
                "aks-managed-type": "aks-slb-managed-outbound-ip",
                "environment": "main",
                "project": "shared-edo",
                "terraform": "true"
            },
            "type": "Microsoft.Network/publicIPAddresses"
        }
        ]
    }

    print(generate(template_type='secops_instance_details', data=example_struct['content']))
    result = generate(template_type=TYPE_PUBLIC_IP_REPORT, data=pip_struct['content'])
    print(result)


if __name__ == '__main__':
    main()
