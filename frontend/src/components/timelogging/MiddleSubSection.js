import React from "react";
import PunchRegion from "./PunchRegion";
import Timer from "./Timer";
import CorrectionRequests from "./CorrectionRequests";

const MiddleSubSection = ({ initialinfo, setInitialinfo }) => {   
    return ( 
        <div className="Subsection">
            <div className="Subsection1">
                <div className="Statusmsg">{initialinfo['live_state'] === 0 ? "You are OUT" : "You are IN"}</div>
                { initialinfo["log_entries"] !== undefined ? <Timer initial_info={initialinfo}/> : null }
                <PunchRegion login_name={initialinfo['login_name']} livestate={initialinfo['live_state']} setInfo={setInitialinfo}/>
            </div>
            <CorrectionRequests initialinfo={initialinfo}/>
        </div>
    );
}

export default MiddleSubSection