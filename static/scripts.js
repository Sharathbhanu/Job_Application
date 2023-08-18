function displayJobResults(jobResults) {
    // Get the container where job results will be displayed
    const jobResultsContainer = document.querySelector(".job-results");
    jobResultsContainer.innerHTML = ""; // Clear previous results

    // Check if job results are available and not empty
    if (jobResults && jobResults.results.length > 0) {
        const job = jobResults.results[0]; // Get the details of the first job

         // Create a div element to display job details
         const jobListing = document.createElement("div");
         jobListing.classList.add("job-listing");

        // Display all details from the first job using template literals
        jobListing.innerHTML = `
            <h2>${job.jobTitle}</h2>
            <p>Job ID: ${job.jobId}</p>
            <p>Employer: ${job.employerName}</p>
            <p>Location: ${job.locationName}</p>
            <p>Salary: ${job.minimumSalary} - ${job.maximumSalary} ${job.currency}</p>
            <p>Expiration Date: ${job.expirationDate}</p>
            <p>Date Posted: ${job.date}</p>
            <p>Job Description: ${job.jobDescription}</p>
            <p>Applications: ${job.applications}</p>
            <a href="${job.jobUrl}" target="_blank">Job Details</a>
        `;
        // Append the job listing to the container
        jobResultsContainer.appendChild(jobListing);
    } else {
        // Display a message if no job results are found
        const noResultsMessage = document.createElement("p");
        noResultsMessage.textContent = "No jobs found.";
        jobResultsContainer.appendChild(noResultsMessage);
    }
}
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