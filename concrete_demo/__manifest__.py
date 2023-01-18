{
    'name': 'Concrete Demo',
    'version': '1.0.0',
    'category': 'Fleet',
    'depends': ['odoo_job_costing_management'],
    'data': [
        'security/ir.model.access.csv',
        # 'views/job_costing_views.xml',
        'views/project_task_view.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
