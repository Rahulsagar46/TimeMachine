import React from "react";
import { DataGrid } from '@mui/x-data-grid';

const CorrectionRequests = ({initialinfo}) => {
    const columns = [
        { field: 'col1', headerName: 'Date', width: 100, headerAlign:'center', headerClassName:'DataGridCols' },
        { field: 'col2', headerName: 'Comment', width: 300, headerAlign:'center', headerClassName:'DataGridCols' },
        { field: 'col3', headerName: 'Status', width: 85, headerAlign:'center', headerClassName:'DataGridCols'},
      ];
    const rows = initialinfo["correction_requests"] === undefined ? [] : initialinfo["correction_requests"].map((row) => ({
        id   : initialinfo["correction_requests"].indexOf(row), 
        col1 : row["request_date"],
        col2 : row["remark"],
        col3 : row["approver_decision"] === -1 ? "pending" : (row["approver_decision"] === 0 ? "rejected" : "approved")
    }));
    return (
        <div className="CorrectionRequestsContainer">
            <div className="DataGridHeader">Correction Requests</div>
            <div className="CorrectionDataGridContainer">
                {initialinfo["correction_requests"] !== undefined ? <DataGrid rows={rows} columns={columns} rowHeight={30} /> : null }
            </div>
        </div>
    )
}

export default CorrectionRequests