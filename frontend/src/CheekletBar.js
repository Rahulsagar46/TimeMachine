import React from "react";
import Cheeklet from './Cheeklet'

const CheekletBar = (props) => {
    return (
        <div>
            <div className="CheekletContainer">
                <Cheeklet />
                <Cheeklet />
                <Cheeklet />
                <Cheeklet />
                <Cheeklet />
                <Cheeklet />
            </div>
        </div>
    );
}

export default CheekletBar