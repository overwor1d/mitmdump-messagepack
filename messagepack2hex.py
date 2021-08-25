class MessagePack2Hex:
    def __init__(self):
        pass

    def response(self, flow):
        if flow.request.url.startswith("https://example.com/"):
            print()
            print(','.join(hex(x) for x in flow.response.content))
            print()

addons = [
    MessagePack2Hex()
]
