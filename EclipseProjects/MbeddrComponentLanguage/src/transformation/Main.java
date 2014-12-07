package transformation;

import java.io.File;
import transformerProcessor.TransformerProcessor;

public class Main {

	public static void main(String[] args) {
		String projectDir = new File(".").getAbsolutePath();
		String transformation = new File("./transformation/mbeddr2C.dsltrans").getAbsolutePath();
		
		try {
			TransformerProcessor tP = new TransformerProcessor(projectDir);
			tP.LoadModel(transformation);
			tP.Execute();
		} catch (Throwable e) {
			System.err.println("Error running transformation: " + transformation);
			e.printStackTrace();
		}
	}

}
