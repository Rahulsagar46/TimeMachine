import React from "react";
import Cheeklet from './Cheeklet'
import {getHoursFromSeconds} from '../../helper'

const CheekletBar = ({initialinfo}) => {
    return (
        <div>
            <div className="CheekletContainer">
                <Cheeklet cheeklet_header='Total Vacation Days' cheeklet_val='28'/>
                <Cheeklet cheeklet_header='Planned Vacation Days' cheeklet_val='10'/>
                <Cheeklet cheeklet_header='Net Working Hours' cheeklet_val={getHoursFromSeconds(initialinfo["net_working_time"])}/>
                <Cheeklet cheeklet_header='KZE' cheeklet_val='01'/>
                <Cheeklet cheeklet_header='Approval pending' cheeklet_val='02'/>
            </div>
        </div>
    );
}

export default CheekletBar