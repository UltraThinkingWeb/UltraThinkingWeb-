import asyncio
import random
import time

class MeshNode:
    def __init__(self, node_id):
        self.node_id = node_id
        self.peers = set()

    async def connect_to_peer(self, peer):
        await asyncio.sleep(random.uniform(0.01, 0.1))  # Simulon vonesën e rrjetit
        self.peers.add(peer)
        return f"Node {self.node_id} connected to Node {peer.node_id}"

    async def broadcast_message(self, message):
        await asyncio.sleep(random.uniform(0.01, 0.1))
        return f"Node {self.node_id} broadcasting: {message}"

async def simulate_mesh_network(num_nodes):
    nodes = [MeshNode(i) for i in range(num_nodes)]
    
    # Simulojmë lidhjet midis nyjeve
    tasks = []
    for node in nodes:
        for _ in range(random.randint(1, 10)):  # Çdo nyje lidhet me 1 deri në 10 peers
            peer = random.choice(nodes)
            if peer != node:
                tasks.append(node.connect_to_peer(peer))

    results = await asyncio.gather(*tasks)

    # Simulojmë dërgimin e një mesazhi nga një nyje
    sender = random.choice(nodes)
    message = "Test Message from Node " + str(sender.node_id)
    broadcast_result = await sender.broadcast_message(message)

    return results, broadcast_result

async def main():
