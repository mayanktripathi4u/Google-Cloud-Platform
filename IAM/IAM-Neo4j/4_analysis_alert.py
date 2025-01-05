def check_independent_users():
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

    with driver.session() as session:
        result = session.run("""
            MATCH (m:Member)-[:HAS_ROLE]->()-[:IN_PROJECT]->(p:Project)
            WHERE NOT m.name STARTS WITH 'group:' AND NOT m.name STARTS WITH 'serviceAccount:'
            RETURN m.name AS user, COLLECT(DISTINCT p.id) AS projects
        """)

        for record in result:
            user = record["user"]
            projects = record["projects"]
            print(f"Alert: Independent user {user} has access to projects: {', '.join(projects)}")

check_independent_users()