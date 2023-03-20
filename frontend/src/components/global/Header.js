import React from 'react';

const Header = (props) => {
    console.log("Header loading")
    const login_name = props['initialinfo']['login_name'];
    const sap_id = props['initialinfo']['sap_id']; 
    return (
        <div>
            <div className="HeaderContainer">
            {/* <div className="Item Item2"><img className="Qlogo" src='qcom_logo.png' alt='logo'/></div> */}
            <div className="Item Item2">LOGO</div>
                <div className="Item Item2">ID:{sap_id}</div>
                <div className="Item Item3">Hello {login_name}</div>
            </div>
        </div>
    );
}

export default Header