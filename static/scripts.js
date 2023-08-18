function searchJobs() {
    const location = document.getElementById("location").value;
    const keywords = document.getElementById("keywords").value;
    const distanceFromLocation = document.getElementById("distanceFromLocation").value;
    const contract = document.getElementById("contract").checked;
    const minimumSalary = document.getElementById("minimumSalary").value;
    const employerId = document.getElementById("employerId").value;
    const searchData = {
        location: location,
        keywords: keywords,
        distanceFromLocation: distanceFromLocation,
        contract: contract,
        minimumSalary: minimumSalary,
        employerId: employerId
    };