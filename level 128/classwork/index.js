const app = express();
const port = 5000;

const connectDb = async () => {
    try {
        const conn = await mongoose.connect(URI);
        console.log('mongodb is connected!: ${await conn.connection.host}');
    }
    catch (err) {
        console.log('mongodb is not connected ${err}');
    }
    
}