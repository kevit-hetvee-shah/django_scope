from scope_agency.agents.scope_agency_individual_agents.main_redefined import generate_graph


class GenerateScopeService:
    def get(self):
        pass

    def post(self, req_query):
        generate_graph(req_query)
