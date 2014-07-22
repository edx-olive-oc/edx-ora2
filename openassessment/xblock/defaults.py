"""Default data initializations for the XBlock, with formatting preserved."""
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long

DEFAULT_PROMPT = """
    Censorship in the Libraries

    'All of us can think of a book that we hope none of our children or any other children have taken off the shelf. But if I have the right to remove that book from the shelf -- that work I abhor -- then you also have exactly the same right and so does everyone else. And then we have no books left on the shelf for any of us.' --Katherine Paterson, Author

    Write a persuasive essay to a newspaper reflecting your views on censorship in libraries. Do you believe that certain materials, such as books, music, movies, magazines, etc., should be removed from the shelves if they are found offensive? Support your position with convincing arguments from your own experience, observations, and/or reading.

    Read for conciseness, clarity of thought, and form.
"""

DEFAULT_RUBRIC_CRITERIA = [
    {
        'name': "Ideas",
        'label': "Ideas",
        'prompt': "Determine if there is a unifying theme or main idea.",
        'order_num': 0,
        'feedback': 'optional',
        'options': [
            {
                'order_num': 0, 'points': 0, 'name': 'Poor', 'label': 'Poor',
                'explanation': """Difficult for the reader to discern the main idea.  Too brief or too repetitive to establish or maintain a focus."""
            },
            {
                'order_num': 1, 'points': 3, 'name': 'Fair', 'label': 'Fair',
                'explanation': """Presents a unifying theme or main idea, but may include minor tangents.  Stays somewhat focused on topic and task."""
            },
            {
                'order_num': 2, 'points': 5, 'name': 'Good', 'label': 'Good',
                'explanation': """Presents a unifying theme or main idea without going off on tangents.  Stays completely focused on topic and task."""
            },
        ],
    },
    {
        'name': "Content",
        'label': "Content",
        'prompt': "Assess the content of the submission",
        'order_num': 1,
        'options': [
            {
                'order_num': 0, 'points': 0, 'name': 'Poor', 'label': 'Poor',
                'explanation': """Includes little information with few or no details or unrelated details.  Unsuccessful in attempts to explore any facets of the topic."""
            },
            {
                'order_num': 1, 'points': 1, 'name': 'Fair', 'label': 'Fair',
                'explanation': """Includes little information and few or no details.  Explores only one or two facets of the topic."""
            },
            {
                'order_num': 2, 'points': 3, 'name': 'Good', 'label': 'Good',
                'explanation': """Includes sufficient information and supporting details. (Details may not be fully developed; ideas may be listed.)  Explores some facets of the topic."""
            },
            {
                'order_num': 3, 'points': 3, 'name': 'Excellent', 'label': 'Excellent',
                'explanation': """Includes in-depth information and exceptional supporting details that are fully developed.  Explores all facets of the topic."""
            },
        ],
    },
]

# The rubric's feedback prompt is a set of instructions letting the student
# know they can provide additional free form feedback in their assessment.
DEFAULT_RUBRIC_FEEDBACK_PROMPT = """
    (Optional) What aspects of this response stood out to you? What did it do well? How could it improve?
"""

DEFAULT_EXAMPLE_ANSWER = """
(optional) Replace this text with your own sample response for this assignment. Below, list the names of the criteria for this assignment, and then specify the name of the option that you would select for this response. Students will learn to assess responses by assessing this response and comparing the rubric options that they select with the rubric options that you specified.

If you don't want to provide sample responses and scores, delete the entire 'assessment name="student-training"' element.
"""

DEFAULT_EXAMPLE_ANSWER_2 = """
(optional) Replace this text with another sample response, and then specify the options that you would select for this response below. To provide more sample responses, copy an "example" element and paste as many as you want before the closing "assessment" tag.
"""

DEFAULT_STUDENT_TRAINING = {
    "name": "student-training",
    "start": None,
    "due": None,
    "examples": [
        {
            "answer": DEFAULT_EXAMPLE_ANSWER,
            "options_selected": [
                {
                    "criterion": "Ideas",
                    "option": "Fair"
                },
                {
                    "criterion": "Content",
                    "option": "Good"
                }
            ]
        },
        {
            "answer": DEFAULT_EXAMPLE_ANSWER_2,
            "options_selected": [
                {
                    "criterion": "Ideas",
                    "option": "Poor"
                },
                {
                    "criterion": "Content",
                    "option": "Good"
                }
            ]
        }
    ]
}

# The Default Peer Assessment is created as an example of how this XBlock can be
# configured. If no configuration is specified, this is the default assessment
# module(s) associated with the XBlock.
DEFAULT_PEER_ASSESSMENT = {
    "name": "peer-assessment",
    "start": None,
    "due": None,
    "must_grade": 5,
    "must_be_graded_by": 3,
}

DEFAULT_SELF_ASSESSMENT = {
    "name": "self-assessment",
    "due": None,
}

DEFAULT_ASSESSMENT_MODULES = [
    DEFAULT_STUDENT_TRAINING,
    DEFAULT_PEER_ASSESSMENT,
    DEFAULT_SELF_ASSESSMENT,
]

DEFAULT_EDITOR_ASSESSMENTS_ORDER = [
    "example-based-assessment",
    "student-training",
    "peer-assessment",
    "self-assessment"
]
