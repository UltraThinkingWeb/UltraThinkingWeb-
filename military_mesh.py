import asyncio
import random

# Definimi i nyjeve sipas hierarkisë ushtarake
class Node:
    def __init__(self, node_id, role, parent=None):
        self.node_id = node_id
        self.role = role
        self.parent = parent
        self.children = []
        self.is_active = True

    async def execute_task(self):
        await asyncio.sleep(random.uniform(0.01, 0.05))  # Simulon detyrën
        print(f"✅ {self.role} {self.node_id} kreu detyrën dhe u fik.")
        self.is_active = False  # Nyja fiket pas përfundimit të detyrës

    async def send_message(self, message):
        if self.parent:
            print(f"📩 {self.role} {self.node_id} dërgon mesazh te {self.parent.role} {self.parent.node_id}: {message}")
            await self.parent.receive_message(message)

    async def receive_message(self, message):
        print(f"�� {self.role} {self.node_id} mori mesazh: {message}")
        if self.parent:
            await self.send_message(message)

# Krijimi i rrjetit Mesh sipas strukturës ushtarake
async def build_military_mesh():
    # Niveli më i lartë: Komanda-Qendrore
    command_center = Node("Komanda-Qendrore", "🌍")

    # Ministri-1 (Lidhet me Komandën Qendrore)
    ministry = Node("Ministri-1", "🏛️", parent=command_center)
    command_center.children.append(ministry)

    # Komanda-1 (Lidhet me Ministrin)
    command1 = Node("Komanda-1", "🏆", parent=ministry)
    ministry.children.append(command1)

    # Divizioni (Lidhet me Komandën-1)
    division = Node("Divizion-1", "⚔️", parent=command1)
    command1.children.append(division)

    # Brigada (Lidhet me Divizionin)
    brigade = Node("Brigada-1", "🏰", parent=division)
    division.children.append(brigade)

    # Batalioni (Lidhet me Brigadën)
    battalion = Node("Batalion-1", "🏛️", parent=brigade)
    brigade.children.append(battalion)

    # Kompanitë (Lidhen me Batalionin)
    companies = [Node(f"Kompania-{i}", "🏅", parent=battalion) for i in range(1, 4)]
    battalion.children.extend(companies)

    # Togat (Lidhen me Kompanitë)
    platoons = [Node(f"Toga-{i}", "🎖️", parent=random.choice(companies)) for i in range(1, 6)]
    for platoon in platoons:
        platoon.parent.children.append(platoon)

    # Ushtarët (Lidhen me Togat)
    soldiers = [Node(f"Ushtar-{i}", "🪖", parent=random.choice(platoons)) for i in range(1, 11)]
    for soldier in soldiers:
        soldier.parent.children.append(soldier)

    # Simulimi i detyrave dhe dërgimit të mesazheve
    tasks = [node.execute_task() for node in soldiers]
    await asyncio.gather(*tasks)

    # Korrierët dërgojnë informacionin në rrjet
    message = "Urdhër nga Komanda-Qendrore!"
    await ministry.send_message(message)

asyncio.run(build_military_mesh())
