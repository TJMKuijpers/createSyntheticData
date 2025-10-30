import yaml


def create_yaml_file_from_dict(information,output):
    data = {
        'Analyst': {
            'name': information['analyst_name'],
            'email': information['analyst_email']
        },
        'Loaded by': information['loaded_by'],
        'Load id': information['load_id'],
        'git id': information['git_id'],
        'Analysis Id': information['analysis_id'],
        'Load Date': information['load_date'],
        'Data Source': information['data_source'],
        'Jira Ticket': information['jira_ticket'],
        'Confluence URL': information['confluence_url'],
        'Study sponsors': information['study_sponsors']
    }

    with open(output, 'w') as file:
        yaml.dump(data, file, default_flow_style=False, sort_keys=False)

if __name__ == '__main__':
    dict_info = {
        'analyst_name': "Jack",
        'analyst_email': "jack@xyz.com",
        'loaded_by': "Jill",
        'load_id': 34,
        'git_id': "xxqaygqertqsg98qhpughqer",
        'analysis_id': "7asdlnagsd98gfaqsgf",
        'load_date': "July 12, 2018",
        'data_source': "Study XY123-456",
        'jira_ticket': "Foo-1",
        'confluence_url': "http://myserver/wxyz",
        'study_sponsors': [
            {'name': 'john', 'email': 'john@@xyz.com'},
            {'name': 'jane', 'email': 'jane@@xyz.com'}
        ],
    }
    create_yaml_file_from_dict(dict_info,'/synthetic_data/study_tags.yml')