def get_customer_support_schema_func():
    return {
        'selection': {
            'page': 'page1',
            'issue': 'issue1',
            'subissue': 'issue1_subissue1',
            'step': 1,
            'item': 'some_product_id'
        },
        'pages': [
            {
                'id': 'page1',
                'label': 'Page 1',
                'steps': [
                    {
                        'id': 'page1_step1',
                        'pre_selection_text': 'Select step 1',
                        'post_selection_text': 'Step 1 selected',
                        'type': 'ISSUES',
                        'issues': [
                            {
                                'id': 'page1_step1_issue1',
                                'label': 'Issue 1',
                                'selection_handler': None,
                                'sub_issues': [
                                    {
                                        'id': 'page1_step1_issue1_subissue1',
                                        'label': 'Sub Issue 1',
                                        'selection_handler': '/some/url/'
                                    }, {
                                        'id': 'page1_step1_issue1_subissue2',
                                        'label': 'Sub Issue 2',
                                        'selection_handler': '/some/url/'
                                    }, {
                                        'id': 'page1_step1_issue1_subissue1',
                                        'label': 'Sub Issue 3',
                                        'selection_handler': '/some/url/'
                                    }
                                ]
                            }, {
                                'id': 'page1_step1_issue1',
                                'label': 'Issue 1',
                                'selection_handler': None,
                                'sub_issues': [
                                    {
                                        'id': 'page1_step1_issue1_subissue1',
                                        'label': 'Sub Issue 1',
                                        'selection_handler': '/some/url/'
                                    }, {
                                        'id': 'page1_step1_issue1_subissue2',
                                        'label': 'Sub Issue 2',
                                        'selection_handler': '/some/url/'
                                    }, {
                                        'id': 'page1_step1_issue1_subissue1',
                                        'label': 'Sub Issue 3',
                                        'selection_handler': '/some/url/'
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        'id': 'page1_step2',
                        'pre_selection_text': 'Select step 2',
                        'post_selection_text': 'Step 2 selected',
                        'type': 'ITEM_SELECTION'
                    },
                    {
                        'id': 'page1_step3',
                        'pre_selection_text': 'Select step 3',
                        'post_selection_text': 'Step 3 selected',
                        'type': 'GET_ASSISTANCE'
                    }
                ]
            }, {
                'id': 'page2',
                'label': 'Page 2',
                'steps': [
                    {
                        'id': 'page2_step1',
                        'pre_selection_text': 'Select step 1',
                        'post_selection_text': 'Step 1 selected',
                        'type': 'ISSUES'
                    },
                    {
                        'id': 'page2_step2',
                        'pre_selection_text': 'Select step 2',
                        'post_selection_text': 'Step 2 selected',
                        'type': 'ITEM_SELECTION'
                    },
                    {
                        'id': 'page2_step3',
                        'pre_selection_text': 'Select step 3',
                        'post_selection_text': 'Step 3 selected',
                        'type': 'GET_ASSISTANCE'
                    }
                ]
            }
        ]
    }

CUSTOMER_SUPPORT_SCHEMA_FUNC = get_customer_support_schema_func
