package transformation;

import java.io.File;
import transformerProcessor.TransformerProcessor;

public class Main {

	public static void main(String[] args) {
		String projectDir = new File("/home/levi/git/TransformationVerificationMbeddr/EclipseProjects/MbeddrComponentLanguage/").getAbsolutePath();
		String transformation = new File("/home/levi/git/TransformationVerificationMbeddr/EclipseProjects/MbeddrComponentLanguage/transformation/mbeddr2C.dsltrans").getAbsolutePath();		
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
