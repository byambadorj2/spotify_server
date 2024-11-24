from fastapi import HTTPException, Header
import jwt


def auth_middleware(x_auth_token = Header()):
    try:
        # get the token from the headers
        if not x_auth_token:
            raise HTTPException(401, detail="No auth token, Access Denied!")

        # decode the token
        verified_token = jwt.decode(x_auth_token, "password_key", ["HS256"])   

        if not verified_token:
            raise HTTPException(401, detail="Token verification failed, auth denied!")
        
        # get the id from the token
        uid = verified_token.get("id")
        return {"uid": uid , "token": x_auth_token}
    except  jwt.PyJWKError:
        raise HTTPException(401, detail="Token verification failed, auth denied!")