import React from 'react';

const Header = (props) => {
    console.log("Header loading")
    const login_name = props['initialinfo']['login_name'];
    const sap_id = props['initialinfo']['sap_id']; 
    return (
        <div>
            <div className="Header">
                <p>Hello {login_name}</p>
            </div>
        </div>
    );
}

export default Header