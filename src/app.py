import os
import json

# Entrypoint of our lambda function
def lambda_handler(event, context):
    
    try:
        
        # Loading environment variables
        def load_envs():
            
            try:
                env_vars = {}
                
                env_vars['ENVIRONMENT'] = os.getenv('ENVIRONMENT')
                env_vars['DB_HOST'] = os.getenv('DB_HOST')
                env_vars['DB_PORT'] = os.getenv('DB_PORT')
                env_vars['DB_USER'] = os.getenv('DB_USER')
                env_vars['DB_PASSWORD'] = os.getenv('DB_PASSWORD')
                
                if env_vars['ENVIRONMENT'] == 'prd':
                    env_vars['AWS_KEY_IAM'] = os.getenv('AWS_KEY_IAM')
                    env_vars['AWS_SECRET_IAM'] = os.getenv('AWS_SECRET_IAM')
                    
                return env_vars
                
            except Exception as e:
                return {
                    'code' : 400,
                    'message' : f'Error occured while loading environment variables: {e}'
                }
        env_vars = load_envs()
        print('\nAll Environment Variables:')
        print([envs for envs in env_vars.values()])
        
        return {
            'code' : 200,
            'message' : 'Lambda Function worked fine'
        }
    except Exception as e:
        return{
            'code' : 400,
            'message' : f'Error occured while executing Lambda Function: {e}'
        }
