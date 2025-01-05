from neo4j import GraphDatabase

def create_graph(iam_data):
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

    with driver.session() as session:
        for data in iam_data:
            project_id = data["project"]
            policy = data["policy"]

            # Create project node
            session.run("MERGE (:Project {id: $project_id})", project_id=project_id)

            for binding in policy.bindings:
                role = binding.role
                for member in binding.members:
                    # Create role and member nodes, and relationships
                    session.run("""
                        MATCH (p:Project {id: $project_id})
                        MERGE (r:Role {name: $role})
                        MERGE (m:Member {name: $member})
                        MERGE (m)-[:HAS_ROLE]->(r)
                        MERGE (r)-[:IN_PROJECT]->(p)
                    """, project_id=project_id, role=role, member=member)

    driver.close()

create_graph(iam_data)