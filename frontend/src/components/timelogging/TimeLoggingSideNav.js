import React from 'react';

const TimeLoggingSideNav = ({ activeTab, setActiveTab }) => {
    return (
        <div className='TimeLoggingSideNavContainer'>
            <div className={activeTab === "timeentry" ? 'SideTabActive' : 'SideTabInactive'} 
                onClick={()=>{
                    setActiveTab("timeentry")
                }}>Time Entry</div>
                <div className={activeTab === "corrections" ? 'SideTabActive' : 'SideTabInactive'}
                onClick={()=>{
                    console.log("came here")
                    setActiveTab("corrections")
                }}>Correction Requests</div>
        </div>
    );
}

export default TimeLoggingSideNav