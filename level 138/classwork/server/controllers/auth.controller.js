export const loginPost = async (req, res) => {
    try {
        res.json({message: "You have successfully logged in"})
    } catch (error){
        res.json({error: error})
    }
}