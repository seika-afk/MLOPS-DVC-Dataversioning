import pandas as pd
import os



data = {
    'Name': ['Python', 'JavaScript', 'C++', 'Java', 'Go', 'Rust', 'Ruby', 'TypeScript', 'Kotlin', 'Swift'],
    'Release Year': [1991, 1995, 1985, 1995, 2009, 2010, 1995, 2012, 2011, 2014],
    'Designed By': [
        'Guido van Rossum',
        'Brendan Eich',
        'Bjarne Stroustrup',
        'James Gosling',
        'Robert Griesemer, Rob Pike, Ken Thompson',
        'Graydon Hoare',
        'Yukihiro Matsumoto',
        'Anders Hejlsberg',
        'JetBrains',
        'Apple Incorporation'
    ],
    'Typing Discipline': [
        'Duck / Dynamic',
        'Duck / Dynamic',
        'Static',
        'Static',
        'Static',
        'Static',
        'Duck / Dynamic',
        'Static',
        'Static',
        'Static'
    ],
    'Current Version': ['3.12', 'ES2023', 'C++20', 'Java 21', '1.22', '1.78', '3.3', '5.4', '1.9', '5.9'],
    'Use Case': [
        'Data Science, Web Dev, AI',
        'Web Dev, Frontend, Backend',
        'Systems Programming, Games',
        'Enterprise Apps, Android Dev',
        'Cloud Computing, DevOps',
        'System Programming, Safety-critical apps',
        'Web Dev, Scripting',
        'Web Dev (Frontend + Backend)',
        'Android Dev, Server-Side',
        'iOS/macOS Apps'
    ]
}

df=pd.DataFrame(data)

data_dir='data'
os.makedirs(data_dir,exist_ok=True)

file_path=os.path.join(data_dir,'sample_data.csv')
df.to_csv(file_path,index=False)

print(f"csv fike saved to {file_path}")
