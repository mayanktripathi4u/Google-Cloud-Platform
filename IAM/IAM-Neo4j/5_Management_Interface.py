from flask import Flask, render_template, request, redirect
from neo4j import GraphDatabase

app = Flask(__name__)
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

@app.route('/')
def index():
    with driver.session() as session:
        result = session.run("""
            MATCH (m:Member)-[:HAS_ROLE]->(r:Role)-[:IN_PROJECT]->(p:Project)
            RETURN m.name AS member, COLLECT(DISTINCT r.name) AS roles, COLLECT(DISTINCT p.id) AS projects
        """)
        iam_data = [dict(record) for record in result]
    return render_template('index.html', iam_data=iam_data)

@app.route('/remove_role', methods=['POST'])
def remove_role():
    member = request.form['member']
    role = request.form['role']
    project = request.form['project']

    with driver.session() as session:
        session.run("""
            MATCH (m:Member {name: $member})-[r:HAS_ROLE]->(role:Role {name: $role})-[:IN_PROJECT]->(p:Project {id: $project})
            DELETE r
        """, member=member, role=role, project=project)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)