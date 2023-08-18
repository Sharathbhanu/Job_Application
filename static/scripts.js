function displayJobResults(jobResults) {
    // Get the container where job results will be displayed
    const jobResultsContainer = document.querySelector(".job-results");
    jobResultsContainer.innerHTML = ""; // Clear previous results

    // Check if job results are available and not empty
    if (jobResults && jobResults.results.length > 0) {
        const job = jobResults.results[0]; // Get the details of the first job
        
function searchJobs() {
    // Get the user input values for search criteria
    const location = document.getElementById("location").value;
    const keywords = document.getElementById("keywords").value;
    const distanceFromLocation = document.getElementById("distanceFromLocation").value;
    const contract = document.getElementById("contract").checked;
    const minimumSalary = document.getElementById("minimumSalary").value;
    const employerId = document.getElementById("employerId").value;

    // Create an object with the search criteria
    const searchData = {
        location: location,
        keywords: keywords,
        distanceFromLocation: distanceFromLocation,
        contract: contract,
        minimumSalary: minimumSalary,
        employerId: employerId
    };