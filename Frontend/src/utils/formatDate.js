export const formatDate = (dateSString) => {
    const date = new Date(dateSString);
    return date.toLocaleDateString();
};