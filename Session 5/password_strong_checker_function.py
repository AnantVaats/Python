def password_strength(password):

    if len(password)<8:
        return "WEAK"
    
    if not any(char.isupper() for char in password):
        return "weak,password must contain atleast one uppercase letter"
    
    if not any(char.islower() for char in password):
        return "weak,password must contain atleast one lowercase letter"
    
    if not any(char.isdigit() for char in password):
        return "weak,password must contain atleast one digit"
    
    return "STRONG"

print(password_strength("Hello!World 98"))