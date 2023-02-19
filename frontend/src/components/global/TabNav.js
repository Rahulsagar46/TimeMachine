import React from 'react';

const TabNav = ({ activeTab, setActiveTab}) => { 
    const isManager = false
    return (
            <div className='TabNav'>
                <div className={activeTab === "timeLoggingTab" ? 'TabActive' : 'TabInactive'} 
                onClick={()=>{
                    setActiveTab("timeLoggingTab")
                }}>Time management</div>
                <div className={activeTab === "vacationManagementTab" ? 'TabActive' : 'TabInactive'}
                onClick={()=>{
                    setActiveTab("vacationManagementTab")
                }}>Vacation management</div>
                
                {/* Load approvals tab only if the user is a manager */}
                {isManager === true ? <div className={activeTab === "approvalsTab" ? 'TabActive' : 'TabInactive'}
                onClick={()=>{
                    setActiveTab("approvalsTab")
                }}>Approvals</div> : null}
            </div>
    );
}

export default TabNav